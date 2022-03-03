package atoi;

public class atoi {
    public int myAtoi(String str) {
        String tmpStr = str.trim();
        int strLength = tmpStr.length();
        if(strLength <= 0) {
            return Integer.MIN_VALUE;
        }

        // check if sign exists.
        boolean minusSignExists = tmpStr.charAt(0) == '-';
        int finalInt = 0;
        for(int i = minusSignExists? 1: 0; i < strLength; i++) {
            if(!Character.isDigit(tmpStr.charAt(i))){
                return finalInt;
            }
            char c = tmpStr.charAt(i);
            int digitValue = ((int)c - '0');
            int makeSureWeDontExceed = (Integer.MAX_VALUE - digitValue) / 10 ;
            if(finalInt < makeSureWeDontExceed) {
                finalInt = finalInt * 10 + ((int)c - '0');
            }
            else {
                return Integer.MIN_VALUE;
            }

        }

        return minusSignExists ? -1 * finalInt: finalInt;
    }
}
