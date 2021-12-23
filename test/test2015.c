#include <check.h>

#include "year2015.h"

START_TEST (test_01) {

    fail_unless(december01() == 0, "December 01 failed.");

} END_TEST

START_TEST (test_02) {

    fail_unless(december02() == 0, "December 02 failed.");

} END_TEST

START_TEST (test_03) {

    fail_unless(december03() == 0, "December 03 failed.");

} END_TEST

START_TEST (test_04) {

    fail_unless(december04() == 0, "December 04 failed.");

} END_TEST

START_TEST (test_05) {

    fail_unless(december05() == 0, "December 05 failed.");

} END_TEST

START_TEST (test_06) {

    fail_unless(december06() == 0, "December 06 failed.");

} END_TEST

START_TEST (test_07) {

    fail_unless(december07() == 0, "December 07 failed.");

} END_TEST

START_TEST (test_08) {

    fail_unless(december08() == 0, "December 08 failed.");

} END_TEST

START_TEST (test_09) {

    fail_unless(december09() == 0, "December 09 failed.");

} END_TEST

START_TEST (test_10) {

    fail_unless(december10() == 0, "December 10 failed.");

} END_TEST

START_TEST (test_11) {

    fail_unless(december11() == 0, "December 11 failed.");

} END_TEST

START_TEST (test_12) {

    fail_unless(december12() == 0, "December 12 failed.");

} END_TEST

START_TEST (test_13) {

    fail_unless(december13() == 0, "December 13 failed.");

} END_TEST

START_TEST (test_14) {

    fail_unless(december14() == 0, "December 14 failed.");

} END_TEST

START_TEST (test_15) {

    fail_unless(december15() == 0, "December 15 failed.");

} END_TEST

START_TEST (test_16) {

    fail_unless(december16() == 0, "December 16 failed.");

} END_TEST

START_TEST (test_17) {

    fail_unless(december17() == 0, "December 17 failed.");

} END_TEST

START_TEST (test_18) {

    fail_unless(december18() == 0, "December 18 failed.");

} END_TEST

START_TEST (test_19) {

    fail_unless(december19() == 0, "December 19 failed.");

} END_TEST

START_TEST (test_20) {

    fail_unless(december20() == 0, "December 20 failed.");

} END_TEST

START_TEST (test_21) {

    fail_unless(december21() == 0, "December 21 failed.");

} END_TEST

START_TEST (test_22) {

    fail_unless(december22() == 0, "December 22 failed.");

} END_TEST

START_TEST (test_23) {

    fail_unless(december23() == 0, "December 23 failed.");

} END_TEST

START_TEST (test_24) {

    fail_unless(december24() == 0, "December 24 failed.");

} END_TEST

START_TEST (test_25) {

    fail_unless(december25() == 0, "December 25 failed.");

} END_TEST

int main(void) {

    Suite *suite = suite_create("Core");
    TCase *testCore = tcase_create("Core");
    SRunner *suiteRunner = srunner_create(suite);
    int numberFailed;

    suite_add_tcase(suite, testCore);
    tcase_add_test(testCore, test_01);
    tcase_add_test(testCore, test_02);
    tcase_add_test(testCore, test_03);
    tcase_add_test(testCore, test_04);
    tcase_add_test(testCore, test_05);
    tcase_add_test(testCore, test_06);
    tcase_add_test(testCore, test_07);
    tcase_add_test(testCore, test_08);
    tcase_add_test(testCore, test_09);
    tcase_add_test(testCore, test_10);
    tcase_add_test(testCore, test_11);
    tcase_add_test(testCore, test_12);
    tcase_add_test(testCore, test_13);
    tcase_add_test(testCore, test_14);
    tcase_add_test(testCore, test_15);
    tcase_add_test(testCore, test_16);
    tcase_add_test(testCore, test_17);
    tcase_add_test(testCore, test_18);
    tcase_add_test(testCore, test_19);
    tcase_add_test(testCore, test_20);
    tcase_add_test(testCore, test_21);
    tcase_add_test(testCore, test_22);
    tcase_add_test(testCore, test_23);
    tcase_add_test(testCore, test_24);
    tcase_add_test(testCore, test_25);

    srunner_run_all(suiteRunner, CK_ENV);
    numberFailed = srunner_ntests_failed(suiteRunner);
    srunner_free(suiteRunner);

    return numberFailed & 1;
}

