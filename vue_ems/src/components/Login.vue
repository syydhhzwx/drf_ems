<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2009/11/20
            <br/>
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          login
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              username:
            </td>
            <td valign="middle" align="left">
              <input v-model="username" type="text" class="inputgri" name="name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              password:
            </td>
            <td valign="middle" align="left">
              <input v-model="password" type="password" class="inputgri" name="pwd"/>
            </td>
          </tr>
        </table>
        <p>
          <input type="submit" class="button" value="登录" @click="user_login"/>
          &nbsp;&nbsp;
          <router-link to="/register">注册</router-link>
        </p>
      </div>
    </div>
    <div id="footer">
      <div id="footer_bg">
        ABC@126.com
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    // 用户登录请求
    user_login() {
      this.axios({
        url: "http://127.0.0.1:8000/app/users/",
        method: "get",
        params: {
          username: this.username,
          password: this.password,
        }
      }).then(res => {
        // 将用户信息保存到sessionStorage方便展示信息
        if (res.data["message"]) {
          console.log(res.data.results["username"]);
          console.log(res.data.results);
          let username = res.data.results["username"];
          sessionStorage.setItem("username", username);
          // 用户登录成功后跳转到首页
          this.$message.success("恭喜你，登录成功")
          this.$router.push("/index");
        }
      }).catch(error => {
        this.$message({
          showClose: true,
          message: '对不起，您输入的用户名或密码有误',
          type: 'error',
          duration: 1000,
        });
      })
    },
  }
}
</script>

<style scoped>

</style>
