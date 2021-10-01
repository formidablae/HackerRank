import java.util.Calendar;

class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        DateFormatSymbols dfs = new DateFormatSymbols(Locale.US);
        String weekdays[] = dfs.getWeekdays();
        
        Calendar cal = new GregorianCalendar(Locale.US);
        cal.set(year, month-1, day);
        return weekdays[cal.get(Calendar.DAY_OF_WEEK)].toUpperCase();
    }
}

