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