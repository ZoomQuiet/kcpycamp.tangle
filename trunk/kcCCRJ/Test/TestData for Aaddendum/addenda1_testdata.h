/* -------------------------------------------------------------------------
//	文件名		：	addenda1_data.h
//	创建者		：	林哲
//	创建时间	：	2008-8-21 12:01:04
//	功能描述	：	用于附录1第4点变量名要用关键字做前缀规范的测试数据，
//					功能实现尚未完整，只包括以下关键字
//	"char":"ch","TCHAR":"ch","bool":"b","BOOL":"b",
//	"int":"n","__int16":"n","__int32":"n","__int64":"n","unsigned":"u",
//	"long":"l","double":"f","float":"f","BYTE":"by","WORD":"w","DWORD":"dw"}
//	
// -----------------------------------------------------------------------*/
#ifndef __8_1 TEST_CHANGE_H__
#define __8_1 TEST_CHANGE_H__

// -------------------------------------------------------------------------

#include <iostream>
using namespace std;
///测试数据使用了我们最常用代码,然后将其中适当的修改



int nAbc, nBcd;
// 1）测试数据1 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确

bool bAbc, bBcd;
// 1）测试数据2 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确

float fAbc, fBcd;
// 1）测试数据3 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果： 正确

double fAbc, fBcd;
// 1）测试数据4 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果： 正确

char chAbc, chBcd;
// 1）测试数据5 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确

WORD wAbc, wBcd;
// 1）测试数据6 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确


DWORD dwAbc, dwBcd;
// 1）测试数据7 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确



char chAc;
int nA = (int)chAc;
unsigned uA = (unsigned)nA;
// 1）测试数据8 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确



int fun1()
{
	int nA = fun2();
}
// 1）测试数据9
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确


float fun1()
{
	char chA;
	int nA, nB;
	chA = (char)nA + (char)nB;
}
// 1）测试数据10 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确


char fun(int asd)
{	
}
// 1）测试数据11 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：错误


int nA, uADS, fQW, chASD;
// 1）测试数据12 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：错误

float nQW, uA, eAS, oEW, lfASF, ufAW;
// 1）测试数据13
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：错误

char chASD, kchQWE, chnER, chfRE;
// 1）测试数据14 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：错误

__int64 nDint64, nDint32;
// 1）测试数据15 
// 2）说明 :变量名要如何正确的命名规范：前缀+类型+名称
// 3）预期结果：正确



// -------------------------------------------------------------------------
// $Log: $

#endif /* __8_1 TEST_CHANGE_H__ */
