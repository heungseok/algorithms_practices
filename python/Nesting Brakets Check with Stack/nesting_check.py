# 괄호들의 sequence를 토큰으로 받아 열린괄호와 닫힌 괄호가 올바르게 입력되었는지를 판별하는 문제.
# 소괄호(‘(‘, ‘)’), 중괄호(‘{‘, ‘}’), 대괄호(‘[‘, ‘]’) 가 섞여서 입력으로 들어온다고 생각하자. 입력이 괄호가 정확히 열리고 닫혀 있는지, 괄호들이 제대로 nesting되어 있는지 검사하는 함수를 작성하라. 편이상 입력은 get_next_token ()을 호출하면 다음과 같은 7 개의 토큰만 반환된다고 가정하면 된다.
#
#   END = 0, /* end of input */
#   LEFT_PARENTHESIS = 1, /* ‘(‘ */
#   RIGHT_PARENTHESIS = 2, /* ‘)’ */
#   LEFT_BRACE = 3, /* ‘{‘ */
#   RIGHT_BRACE = 4, /* ‘}’ */
#   LEFT_BRACKET = 5, /* ‘[‘ */
#   RIGHT_BRACKET = 6 /* ‘]’ */
#
# 정상적인 입력으로 판정되면 0을, 그렇지 않다면 1을 반환하면 된다.


# Main solution: Stack의 push와 pop을 이용해서 sequence에서 열린괄호가 들어왔을 경우 push, 닫힌 괄호가 들어올 경우 열린괄호가 마지막 인덱스에 있을 경우 pop.

# 닫힌괄호에 대응되지 않는 열린괄호가 마지막 인덱스에 있을 경우는 false, ex: {]]}
# token을 마지막까지 check했을 때 stack에 남아있는 element가 있다면 (열린괄호가 남아있다면) false

def get_next_token():
    # *** wrong cases ***
    # return [1,6,0]
    # return [1,5,1,2,6,2,3,6,6,4,0]
    # return [1, 3, 2, 4, 0]
    # return [4, 3, 0]
    # return [3,6,6,4,0]

    # *** true cases ***
    # return [1, 2, 0]
    return [1,3,4,3,3,4,4,5,1,2,6,2,0]


def test_nesting(tokens):
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
    print(test_nesting(get_next_token()))

if __name__ == "__main__":
    main()

