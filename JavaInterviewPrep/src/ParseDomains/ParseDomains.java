package ParseDomains;

import java.util.*;


// Write a function that takes this input as a parameter and returns a data structure containing
// the number of hits that were recorded on each domain AND each domain under it.
// For example, an impression on "sports.yahoo.com" counts for "sports.yahoo.com", "yahoo.com", and "com".
// (Subdomains are added to the left of their parent domain. So "sports" and "sports.yahoo" are not valid domains.)


// Expected output (in any order):
// 1320    com
//  900    google.com
//  410    yahoo.com
//   60    mail.yahoo.com
//   10    mobile.sports.yahoo.com
//   50    sports.yahoo.com
//   10    stackoverflow.com
//    3    org
//    3    wikipedia.org
//    2    en.wikipedia.org
//    1    es.wikipedia.org


class Solution {
    public static void main(String[] args) {
        String[] counts = {
                "900,google.com",
                "60,mail.yahoo.com",
                "10,mobile.sports.yahoo.com",
                "40,sports.yahoo.com",
                "300,yahoo.com",
                "10,stackoverflow.com",
                "2,en.wikipedia.org",
                "1,es.wikipedia.org"
                // "0,web.bilkent.edu.tr",
                // "12,a.b.c.d.e.f.com.tr",
                // "12.a.b.c.d.e.f.com.tr", // NOT HANDLED

        };
        // 12 d.e.f.com.tr
        // 12 e.f.com.tr

        System.out.println(parse(counts));
    }

    public static Map<String, Integer> parse(String[] arr) {
        Map<String, Integer> mp = new HashMap();

        Map<String, Integer> commaSplittedMap = new HashMap<>();
        for(String str: arr) {
            String[] commaSplitted = str.split(",");
            commaSplittedMap.put(commaSplitted[1], Integer.valueOf(commaSplitted[0]));
        }

        Set<Map.Entry<String, Integer>> es = commaSplittedMap.entrySet();
        for(Map.Entry<String, Integer> entry: es) {

            //create new string, integer
            String[] stringSeparated = entry.getKey().split("\\.");

            Stack<String> partials = new Stack();
            for(int i = stringSeparated.length - 1; i >= 0; i--) {
                String str = "";
                if(!partials.isEmpty()) {
                    str = partials.peek();
                }

                String newStr = "";
                if(!str.isEmpty()) {
                    newStr = stringSeparated[i] + "." + str;
                }
                else {
                    newStr = stringSeparated[i];
                }

                partials.push(newStr);

                mp.put(newStr, mp.getOrDefault(newStr, 0) + entry.getValue());
            }
        }
        return mp;
    }
}
