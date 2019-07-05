#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define a 97
#define z 122
#define A 65
#define Z 90
#define SPACE 32
#define NO0 48
#define NO9 57

void reverse_a_string(char * str) {
    printf("\nInput String: %s", str);
    int n = strlen(str);
    int i = 0, j = n-1;
    while(i <= j) {
        char temp = str[j];
        str[j] = str[i];
        str[i] = temp;
        i++;
        j--;
    }
    printf("\tReversed String: %s", str);
}

bool check_if_pangram(char * str) {
    printf("\nInput String: %s", str);
    int n = strlen(str);
    int index, count = 0;
    bool lookup_array[26];
    memset(&lookup_array, false, 26);

    for(int i=0; i<n; i++) {
        if ((a <= str[i]) && (str[i] <= z)) {
            index = str[i] - a;
        } else if ((A <= str[i]) && (str[i] <= Z)) {
            index = str[i] - A;
        } else {
            continue;
        }
        if (!lookup_array[index]) {
            count++;
            lookup_array[index] = true;
        }
    }
    if (count == 26) return true;
    return false;
}

void missing_characters_for_pangram(char * str) {
    printf("\nInput String: %s", str);
    int n = strlen(str);
    int index, count = 0;
    bool lookup_array[26];
    memset(&lookup_array, false, 26);

    for(int i=0; i<n; i++) {
        if ((a <= str[i]) && (str[i] <= z)) {
            index = str[i] - a;
        } else if ((A <= str[i]) && (str[i] <= Z)) {
            index = str[i] - A;
        } else {
            continue;
        }
        if (!lookup_array[index]) {
            count++;
            lookup_array[index] = true;
        }
    }
    printf("\nMissing characters: ");
    for(int i=0; i< 26; i++) {
        if (!lookup_array[i]) {
            printf(" %c", i + a);
        }
    }
}

#define IS_PUNCTUATION(ch)                      \
    !(((a <= (ch)) && ((ch) <= z)) ||           \
      ((A <= (ch)) && ((ch) <= Z)) ||           \
      ((NO0 <= (ch)) && ((ch) <= NO9)) ||       \
      ((ch) == SPACE))                          \

void remove_punctuation(char * str) {
    printf("\nInput String: %s", str);
    int n = strlen(str);
    int index = 0;
    for (int i = 0; i < n; i++) {
        if (IS_PUNCTUATION(str[i])) {
            continue;
        } else {
            str[index] = str[i];
            index++;
        }
    }
    str[index] = '\0';
    printf("\nModified String: %s", str);
}


int main()
{
    char str[100] = "!The&../ United *States* of //America!?";
    //reverse_a_string(str);
    //printf("\nThe string %s pangram. ", check_if_pangram(str) ? "is" : "is not");
    //missing_characters_for_pangram(str);
    remove_punctuation(str);
    return 1;
}
