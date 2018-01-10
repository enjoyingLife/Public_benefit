 $(function(){
 //入口函数开始
        // ‘申请项目按钮’ 跳转到显示申请页面
        $('#apply').click(function(){
            location.href = "/pro_action/show_apply"
        });


 //------------------三级联动省市县----------------------

    // 发起一个ajax get请求，访问/prov，获取所有省级地区的json信息
    $.get('/user/prov', function (data) {
        // 获取返回的json信息
        var areas = data.res;


        //=========================测试区============================

        //=====================================================
        // 获取prov下拉列表框
        var prov = $('#prov')

        // 遍历areas把省级地区的信息添加到prov下拉列表框中
        $.each(areas, function (index, item) {
            var option_str = '<option name="a" value="' + item[0] + '">' + item[1] + '</option>'
            prov.append(option_str)
        })
    });

    //  定义全局变量接收用户选择的 prov省 city市 dis县
    var ppid = '';
    var cpid = '';
    var dpid = '';
    var prov_select = '';
    var city_select = '';
    var dis_select = '';

    // alert('2')
    $('#prov').change(function () {
        // 获取点击的省id
        ppid = $(this).val();
        prov_select = $('#prov option:selected').text();
        // alert('3');
        // alert(prov_select);
        // alert(ppid);
        // 发起ajax get请求，请求/city/省id, 获取省下面的市级地区的json信息
        $.get('/user/city/'+ ppid, function (data) {
            // 获取返回的json信息
            var areas = data.res;

            // 获取city下拉列表框
            var city = $('#city');
            // 清空city下列表框
            city.empty().append('<option>----请选择市-----</option>');

            // 获取dis下拉列表框
            var dis = $('#dis');
            // 清空dis下列表框
            dis.empty().append('<option>----请选择县-----</option>');

            // 遍历areas把市级地区的信息添加到city下拉列表框中
            $.each(areas, function (index, item) {
                var option_str = '<option value="' + item[0] + '">' + item[1] + '</option>'
                city.append(option_str)
            })
        })
    });

    $('#city').change(function () {
        // 获取市id
        cpid = $(this).val();
        city_select =$('#city option:selected').text();
        // alert(city_select);
        // alert(cpid);
        // 发起ajax get请求，请求/dis/市id, 获取市下面的县级地区的json信息
        $.get('/user/dis/'+cpid, function (data) {
             // 获取返回的json信息
            var areas = data.res;

            // 获取dis下拉列表框
            var dis = $('#dis');

            // 清空dis下列表框
            dis.empty().append('<option>----请选择县-----</option>');

            // 遍历areas把市级地区的信息添加到city下拉列表框中
            $.each(areas, function (index, item) {
                var option_str = '<option value="' + item[0] + '">' + item[1] + '</option>'
                dis.append(option_str)
            })

        })
    });

    $("#dis").change(function () {
        dpid = $(this).val();
        dis_select = $('#dis option:selected').text();
        // alert(dis_select);
    });


//-----------------注册部分------------------------------

    //保证一部分：不失去焦点直接点注册按钮也不让通过注册
    var error_user_name = true;
    var error_pwd = true;
    //一个开关flag

    var is_right1 = false;
    var is_right2 = false;
    var is_right3 = false;


    var user_name = $('#user_name');
    var pwd = $('#pwd');
    var cpwd = $('#cpwd');
    //验证用户名
    user_name.blur(function(){
        check_user_name();
    });

    //验证密码
    pwd.blur(function(){
        check_pwd();
    });

    //俩次密码验证
    cpwd.blur(function () {
       check_cpwd();
    });

    $('.reg_sub input').click(function () {
        if(is_right1 == true && is_right2== true){
            // alert('12')

            var user_names = $('#user_name').val();
            var pwds = $('#pwd').val();
            try {
                var csrf = $('input[name="csrfmiddlewaretoken"]').val();

            //====将省市县数据和用户注册数据一起保存变量中发送到后台======
                var res = {
                   //----注册表中的数据-----
                    'user_name': user_names,
                    'pwd':pwds,
                    'csrfmiddlewaretoken': csrf,

                    //----省市县的数据-----
                    'ppid': ppid,
                    'cpid': cpid,
                    'dpid': dpid,
                    'prov_select_val': prov_select,
                    'city_select_val': city_select,
                    'dis_select_val' : dis_select,
                };

               $.ajax({
                   'url':'/user/add',
                   'type':'post',
                   'data': res,
               }).success(function (data) {
                   // alert(data);
                   location.href = '/'
               });
                // alert('3')
                // location.href= '/add'
            }
            catch (error){
                alert(error)
            }
            }
        else {
            alert("很遗憾！输入格式不正确，请重新输入");
            location.href ='/user/show_register'
        }
    });

// alert($('#allow').prop('checked'))  == true / false


    //自定义函数保存各个命令
    //验证用户名函数
    function check_user_name(){
    // alert(1)
        //1、列正则表达式
        //2、获取用户输入的数据
        // var reg = /^\w{6,20}$/;
        // var reg = /^[a-zA-Z]{1}([a-zA-Z0-9_]){4,14}$/;
        var reg = /^[^ 0-9a-zA-Z]{2,7}$/;
        // [u4e00-u9fa5]
        var val = user_name.val();
        // alert( reg.test(val) )
        //判断为空的情况
        if(val == '')
        {
            // alert(）
            //显示提示信息，并内容是用户名不能为空
            user_name.next().show();
            user_name.next().html('用户名不能为空');
            return;
        }
        if(reg.test(val))
        {
            // alert('ok')
            //隐藏提示信息
            user_name.next().hide();
            //打开开关  通过
            error_user_name = false;
            is_right2 = true;
            // alert('判断用户名----' + is_right2)

        }
        else
        {
            //显示错误 -- 错误信息的表示显示-- 改变这个标签的内容
            user_name.next().show();
            // user_name.next().html('用户名是6到15个英文或数字，还可包含“_”');
            user_name.next().html('用户名为2到7位的中文');
            //关闭开关  不通过
            error_user_name = true;
                    // alert('判断用户名-----'+ is_right2)


        }
}

    //验证密码的函数
    function check_pwd(){
    var reg = /^[\w!@#$%^&*]{6,20}$/; 
    var val = pwd.val();
    if(val == ''){
        pwd.next().show();
        pwd.next().html('密码不能为空');
        return;
    }
    if(reg.test(val))
    {
        pwd.next().hide();
        error_pwd = false;
        is_right1 = true;
    }
    else
    {
        //显示错误 -- 错误信息的表示显示-- 改变这个标签的内容
        pwd.next().show();
        pwd.next().html('密码是6到15位字母、数字，还可包含@!#$%^&*字符');
        error_pwd = true;
    }
}

    function check_cpwd() {
    var pwd_val = pwd.val();
    var cpwd_val = cpwd.val();
    if(pwd_val == cpwd_val){
        cpwd.next().hide();
        is_right3 =true;

    }
    else {
        cpwd.next().show();
        cpwd.next().html('俩次密码输入不正确');
        error_pwd = true;
    }
}
















// 入口函数结尾
 });