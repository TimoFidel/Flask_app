
function Validate()
{
    if (ValidateEmail() && ValidatePassword())
    {
        return true
    }
    else{
        return false
    }
}





function ValidatePassword(password)
{
    var passw=  /^[A-Za-z]\w{7,14}$/ ;
    var y = document.forms["myform"]["password"].value;
    if (passw.test(y) == true)
    {
        return true
    }
    else
    {
        alert("Enter valid Password")
        return false
    }
}





function ValidateEmail(mail)
{
    var reg = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var x=document.forms["myform"]["mail"].value;
    if(reg.test(x)==true)
    {
        return true
    }
    else{
        alert("Enter valid emailID")
        return false
    }
}