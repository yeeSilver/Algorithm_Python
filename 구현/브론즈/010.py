'''
이스케이프 문자에 관한 문제들

개를 출력하시오 
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''
print(
    '|\_/|\n|q p|   /}\n( 0 )"""\\\n|"^"`    |\n||_/=\\\__|'
)

# \\n의 경우 \\가 연속으로 있어서 \n을 인식하지 못한다.백 슬러시(＼) 두 개가 있으면 하나의 백 슬러시만 출력되는 성질이 있기 때문. 이것을 방지하기 위해서 앞에 백 슬래시를 한번 더 붙여준 것이다. 백 슬래시를 두 개 출력하기 위해선 백 슬래시를 하나 더 붙여주게 되면 백 슬래시가 두 개가 출력된다.
# ("||_/=\\\__|")  # \\ 앞에 \을 하나 더 붙여준다.

'''
10171) 고양이를 출력하시오
\    /\
 )  ( ')
(  /  )
 \(__)|

'''
# 따옴표를 넣고 싶을때는 \" -> 큰 따옴표
# \를 이스케이프 문자가 아니라 그대로 출력하고 싶을 때 -> print(r'(여기에 출력할 str넣기)') 로 하면된다.
print('\    /\\\n )  ( \')\n(  /  )\n \(__)|')
