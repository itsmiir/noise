public class JNIHelloWorld {
    // static {
    // }

    private native void test(int i);

    public static void main(String[] args) {

        System.loadLibrary("foo");
        new JNIHelloWorld().test(10);
    }
}