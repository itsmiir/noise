#include "JNIHelloWorld.h"

extern "C" void test(int64_t);

JNIEXPORT void JNICALL Java_JNIHelloWorld_test(JNIEnv* env, jobject obj, jint i) {
    test(i)
  }