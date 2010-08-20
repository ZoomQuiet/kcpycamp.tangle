function check(myform) {
	var ipt;
	var textboxs = new Array(); // text类型的input集合
	var inputs = myform.getElementsByTagName("INPUT"); // 取form下的所有input
	for (var i=0; i<inputs.length; i++)
	{
		ipt = inputs[i];
    		if (ipt.type == "text" || ipt.type == "password")
    		{
      			textboxs[textboxs.length] = ipt;
    		}
	}
  	for (var i=0; i<textboxs.length; i++)
  	{
    		var txt = textboxs[i];
    		if (txt && txt.value == "")
    		{
      			alert("Please Enter The:" + txt.name);
      			txt.focus();
      			return false;
    		}
  	}

	userPassword = myform.password.value;
	userCpassword = myform.cpassword.value;

	if(userPassword != userCpassword)
	{
		alert("两次输入密码不正确请重新输入");
		return false;
	}

	userID = myform.id.value;
	if(check_userID(userID) == false)
            return false;
	
}

function check_userID(userID)
{
	var len = userID.length;
	if(len > 18)
	{
		alert("登陆ID不能超过18个字符!");
		return false;
	}
        var stop_chars = '!$?)(*&?%$/"';
	
        for(i=0;i<stop_chars.length;i++)
        {
            c = stop_chars.charAt(i);
            if(userID.indexOf(c) != -1)
            {
                alert("登陆ID不能插入"+c+" 请重新输入!");
                return false;
            }
        }
        return true;
}

