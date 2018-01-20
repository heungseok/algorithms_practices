def get_next_token():
    # *** wrong cases ***
    # return [1,6,0]
    # return [1,5,1,2,6,2,3,6,6,4,0]
    # return [1, 3, 2, 4, 0]
    # return [4, 3, 0]

    # *** true cases ***
    # return [1, 2, 0]
    return [1,3,4,3,3,4,4,5,1,2,6,2,0]


def test_nesting(tokens):
    brakets_dic = {2:1, 4:3, 6:5}
    stack = []


def test_nesting_wrong_answer(tokens):
    brakets_dic = {2:1, 4:3, 6:5}
    stack = []
    for token in tokens:
        if token == 0:
            if len(stack) == 0:
                return 0
            # token이 0이면서 stack에 element가 아직 남아있다면 부적절한 input
            else:
                return 1
        else:
            if token in brakets_dic: # dictionary에 token을 key값이 있는 경우를 check => token input이 닫힌 괄호인지를 check
                _val = brakets_dic[token] # token을 key값으로 가지는 value (열린괄호) 를 _val로 assign
                if len(stack) == 0:
                    stack.append(_val)
                else:
                    # token에 대응하는 열린괄호가 stack의 마지막 인덱스에 있을 경우 pop
                    if stack[len(stack)-1] == _val:
                        stack.pop()
                    # 그렇지 않을 경우(대응하는 열린부호가 마지막 인덱스에 없는 경우): 열린괄호가 stack에 안들어왔으므로 false return
                    else:
                        return 1
                        # stack.append(_val) # wrong answer

            else: # dict에 token key값이 없는 경우 (value, 즉 input이 열린 괄호인 경우), 열린괄호 먼저 push
                stack.append(token)


def main():
    print(test_nesting_wrong_answer(get_next_token()))

if __name__ == "__main__":
    main()

