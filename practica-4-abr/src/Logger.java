import java.io.PrintStream;

public final class Logger {
    private static Level level;
    private static PrintStream streamOut;
    public enum Level {
        INFO, WARN, ERROR
    }

    private Logger()
    {

    }
    public static void config(Level level, PrintStream streamOut) {
        Logger.level = level;
        Logger.streamOut = streamOut;
    }
    public static void showInfo(String msg) {
        if (Logger.level.ordinal() <= Level.INFO.ordinal()) {
            showMsgWithHeader(Level.INFO.name(), msg);
        }
    }
    public static void showWarn(String msg) {
        if (Logger.level.ordinal() <= Level.WARN.ordinal()) {
            showMsgWithHeader(Level.WARN.name(), msg);
        }
    }
    public static void showError(String msg) {
        if (Logger.level.ordinal() <= Level.ERROR.ordinal()) {
            showMsgWithHeader(Level.ERROR.name(), msg);
        }
    }
    private static void showMsgWithHeader(String header, String msg) {
        Logger.streamOut.println(header + ": " + msg);
    }
}