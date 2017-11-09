import java.net.*;
import java.io.*;
import java.util.ArrayList;
import java.util.regex.*;
import java.util.Locale;


/*
  Parse Debarment DB Dump for matching clients
  An individual's record looks like:

  <tr>
     <td valign="top">STEFFENS, PAUL<br>1778 CALICO LANE<br>TOMS RIVER, NJ 08753<br><br>NPI-</td>
     <td valign="top">Medical<br>Criminal Offense</font></td>
     <td valign="top">Debarment<p>Human Services<br>Medical Assistance (Medicaid)</font></td>
     <td valign="top">4/23/2003</font></td>
     <td valign="top"><br></font></td>
  </tr>
*/

public class DumpDebarDB {
    public static void main(String[] args) throws Exception {
        String search = "=============================Searching==============================\n";
        String bar = "====================================================================\n";
        String addr = "https://www.state.nj.us/cgi-bin/treas/revenue/debarsearch.pl";
        String desktop = System.getProperty("user.home") + "/Desktop";
        File clientlist = new File(desktop + "/clients.txt");
        if (!clientlist.exists()) {
            System.out.printf("Cannot find %s, exiting\n", clientlist);
            System.exit(1);
        }

        boolean RecordStart = false; 
        ArrayList<String> record = new ArrayList<String>();
        URL url = new URL(addr);
        URLConnection conn = url.openConnection();
        BufferedReader in = new BufferedReader(
            new InputStreamReader(conn.getInputStream())
        );
        
        String line;
        System.out.println(search);
        while ((line = in.readLine()) != null)
            if (!RecordStart) {
                Matcher start = Pattern.compile("\\s*<tr>\\s*$").matcher(line);
                RecordStart = start.find();
            } else {
                if (record.isEmpty()) {
                    BufferedReader br = new BufferedReader(new FileReader(clientlist));
                    for (String client = br.readLine(); client != null; client = br.readLine()) {
                        if (line.toLowerCase().contains(client.toLowerCase())) {
                            record.add(line);
                        }
                    }
                    br.close();
                } else {
                    Matcher RecordEnd = Pattern.compile("\\s*</tr>\\s*$").matcher(line);
                    if (RecordEnd.find()) {
                        for (int i = 0; i<record.size(); i++) {
                            System.out.println(record.get(i));
                        }
                        record.clear();
                        System.out.println(bar);
                    } else {
                        record.add(line);
                    }
            }
        }
                
                
        in.close();
    }
}

