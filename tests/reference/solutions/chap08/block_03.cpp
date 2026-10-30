// 削除するノード v の直前のノード p が見つかったことを全体にする
void erase(Node *v, Node *p) {
    if (v == nil) return;  // v が番兵時は何もしない
    p->next = v->next;
    delete v;
}
