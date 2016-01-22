#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#汉诺塔游戏
#递归算法实现

def move(n, a, b, c):
	if n == 1:
		print(a,'-->',c)
	else :
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
	return   

move(3, 'A', 'B', 'C')

2 ABC > 1 ACB  -AB
2 ABC 				 -AC
2 ABC > 1 BAC	 -BC

3 ABC > 2 ACB >1 ABC  - AC
			  1 ACB					- AB
			  1 CAB					- CB
3 ABC 								- AC
3 ABC > 2 BAC > 1 BCA	- BA
				1 BAC 				- BC
				1	ABC					- AC

4 ABC > 3 ACB > 2 ABC > 1 ACB		-AB
								1 ABC						-AC
								1 BAC						-BC
				3 ACB 									-AB	
				3 ACB	> 2 CAB > 1 CBA		-CA
								1 CAB						-CB	
								1 ACB						-AB
4 ABC														-AC
4 ABC	> 3 BAC > 2 BCA > 1 BAC		-BC
								1 BCA						-BA
								1 CBA						-CA
				3 BAC										-BC
				3 BAC > 2 ABC > 1 ACB		-AB
								1 ABC						-AC
								1 BAC						-BC



