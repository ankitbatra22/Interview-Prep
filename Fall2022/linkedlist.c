#include <stdlib.h>
#include <stdio.h>
#include "linked_list.h"

/*******************************************************************************
* Useful Debugging Functions
*******************************************************************************/
void print(node_t* node) {
  printf("(%d, %d)", node->x, node->y);
}

void printAll(node_t* head) {
  node_t *current_node = head;
  while ( current_node != NULL) {
    print(current_node);
    current_node = current_node->next;
  }
  printf("\n\n");
}

/*******************************************************************************
* Data structure operations
*******************************************************************************/
void dequeue(linked_list_t* list) {
  node_t* last = list->end;
  list->end = list->end->prev;
  list->end->next = NULL;
  free(last);
}

void pushFront(linked_list_t* list, node_t* node) {
  node_t* first = list->start;
	list->start = node;
	list->start->next = first;
	first->prev = list->start;
	list->start->prev = NULL;
}

void pushEnd(linked_list_t* list, node_t* node) {
  node_t* last = list->end;
  list->end = node;
  list->end->prev = last;
  last->next = list->end;
  list->end->next = NULL;
}

void clearList(linked_list_t* list) {
  node_t* tmp;
  node_t* node = list->start;

  while (node != NULL) {
    tmp = node;
    node = node->next;
    free(tmp);
  }

  list->start = NULL;
  list->end = NULL;
}



ode_t*    a = (node_t*) malloc(sizeof(node_t));
    node_t*    b = (node_t*) malloc(sizeof(node_t));
    node_t*    c = (node_t*) malloc(sizeof(node_t));
    node_t*    d = (node_t*) malloc(sizeof(node_t));
    node_t*    e = (node_t*) malloc(sizeof(node_t));
    node_t*    f = (node_t*) malloc(sizeof(node_t));

    a->x = 160;
    a->y = 120;
    a->prev = NULL;
    b->x = 150;
    b->y = 120;
    b->next = NULL;
    a->next = b;
    b->prev = a;

    tail.start = a;
    tail.end = b;

    c->x = 140;
    c->y = 120;
    d->x = 130;
    d->y = 120;
    e->x = 120;
    e->y = 120;
    f->x = 110;
    f->y = 120;