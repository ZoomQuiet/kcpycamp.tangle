/* -------------------------------------------------------------------------
//	文件名		：	8.1 test_change.h
//	创建者		：	邢佳
//	创建时间	：	2008-8-18 23:01:04
//	功能描述	：	用于检测8.1代码规范的例程(自编)
//
//	$Id: $
// -----------------------------------------------------------------------*/
#ifndef __8_1 TEST_CHANGE_H__
#define __8_1 TEST_CHANGE_H__

// -------------------------------------------------------------------------

#include <iostream>
using namespace std;
///测试数据使用了我们最常用的一下代码,然后将其中适当的修改

enum{up, down, left, right};
// 1）测试数据1 


enum {up1, down1, left1, 
righk};
// 1）测试数据2 


enum 
{up11, down11, left11, 
righk1};
// 1）测试数据3


enum 
{
	up3111, down111, left1101, 
righk121};
// 1）测试数据4 


	enum 
	{
	up1101, dow3n111, left1611, 
righk11
	};
// 1）测试数据5 


	enum 
	{///注释 
	up1111, down1111, left1111, 
righk111
	};
// 1）测试数据6 


	enum 
	{
		down0111, left111, 
		righk101,
up10};
// 1）测试数据7 



enum{
	up2,
		down2,
		left2,
		right2
	};
// 1）测试数据8 

enum{///注释
	up62,
		down52,
		left26,
		right23
	};
// 1）测试数据8 




	
	enum
	{up3,
	down3,
	left3,
	right3
	};
// 1）测试数据9 


		enum
/*注释*/{
	 up4,
	down4,
	left4,
	right4
		};
// 1）测试数据10 


		enum{ /*注释*/ hello,
hello2,hello3}
// 1）测试数据11 


		enum
		{ /*注释*/ hello1,hello12,hello13}
// 1）测试数据12 


		enum
			{ /*注释*/ hello11,hello112,hello113
			}
// 1）测试数据13 

												enum
													{ 
				  /*注释*/ hello01,hello012,hello013}
// 1）测试数据14 




// -------------------------------------------------------------------------
// $Log: $

#endif /* __8_1 TEST_CHANGE_H__ */
