#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure for Book
struct Book {
    int id;
    char title[50];
    char author[50];
    struct Book* next;
};

struct Book* head = NULL;

// Add Book
void addBook() {
    struct Book* newBook = (struct Book*)malloc(sizeof(struct Book));

    printf("Enter Book ID: ");
    scanf("%d", &newBook->id);
    getchar();

    printf("Enter Title: ");
    fgets(newBook->title, 50, stdin);

    printf("Enter Author: ");
    fgets(newBook->author, 50, stdin);

    newBook->next = head;
    head = newBook;

    printf("Book Added Successfully!\n");
}

// Display Books
void displayBooks() {
    struct Book* temp = head;

    if (temp == NULL) {
        printf("No books available!\n");
        return;
    }

    printf("\nLibrary Books:\n");
    while (temp != NULL) {
        printf("ID: %d", temp->id);
        printf("Title: %s", temp->title);
        printf("Author: %s\n", temp->author);
        temp = temp->next;
    }
}

// Search Book
void searchBook() {
    int id;
    printf("Enter Book ID to search: ");
    scanf("%d", &id);

    struct Book* temp = head;

    while (temp != NULL) {
        if (temp->id == id) {
            printf("Book Found!\n");
            printf("Title: %s", temp->title);
            printf("Author: %s\n", temp->author);
            return;
        }
        temp = temp->next;
    }

    printf("Book not found!\n");
}

// Delete Book
void deleteBook() {
    int id;
    printf("Enter Book ID to delete: ");
    scanf("%d", &id);

    struct Book *temp = head, *prev = NULL;

    if (temp != NULL && temp->id == id) {
        head = temp->next;
        free(temp);
        printf("Book Deleted!\n");
        return;
    }

    while (temp != NULL && temp->id != id) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Book not found!\n");
        return;
    }

    prev->next = temp->next;
    free(temp);
    printf("Book Deleted!\n");
}

// Main Function
int main() {
    int choice;

    while (1) {
        printf("\n--- Library Management System ---\n");
        printf("1. Add Book\n");
        printf("2. Display Books\n");
        printf("3. Search Book\n");
        printf("4. Delete Book\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: addBook(); break;
            case 2: displayBooks(); break;
            case 3: searchBook(); break;
            case 4: deleteBook(); break;
            case 5: exit(0);
            default: printf("Invalid choice!\n");
        }
    }

    return 0;
}