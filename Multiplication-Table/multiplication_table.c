#include <stdio.h>
#include <stdbool.h>
int main() {
	printf("Multiplication table\n---------------------");
	int user_input;

	while (true) {
		printf("\n\nTable of : ");
		scanf("%d", &user_input);

		for (int i = 1; i <= 10; i++) {
			printf("\n%d × %d = %d", i, user_input, i * user_input);
		}
	}

	return 0;
}