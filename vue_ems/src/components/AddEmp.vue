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
            <a href="#">Main</a>
            <span>当前用户名：{{user}}</span>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          add Emp info:
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              name:
            </td>
            <td valign="middle" align="left">
              <input v-model="username" type="text" class="inputgri" name="name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              photo:
            </td>
            <td valign="middle" align="left">
              <!--             文件框是只读的  无法用v-model进行绑定               -->
              <input ref="photo" type="file" name="photo"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              salary:
            </td>
            <td valign="middle" align="left">
              <input v-model="salary" type="text" class="inputgri" name="salary"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              age:
            </td>
            <td valign="middle" align="left">
              <input v-model="age" type="text" class="inputgri" name="age"/>
            </td>
          </tr>
        </table>
        <p>
          <el-button type="primary" @click="add_emp">确定添加</el-button>
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
  name: "AddEmp",
  data() {
    return {
      username: "",
      photo: "",
      salary: "",
      age: "",
      user:''
    }
  },
  methods: {
    // 添加员工
    add_emp() {
      // 获取文件信息
      // console.log(this.$refs.photo.files[0]);

      // 文件上传时请求方式必须是post  且enctype必须是 multipart/form-data
      // 使用ajax上传文件时，必须借助于formData

      let formData = new FormData();
      formData.append("emp_name", this.username)
      formData.append("salary", this.salary)
      formData.append("age", this.age)
      formData.append("img", this.$refs.photo.files[0])

      this.axios({
        url: "http://127.0.0.1:8000/app/employeess/",
        method: "post",
        data: formData,
        headers: {
          "content-type": "multipart/form-data"
        },
      }).then(res => {
        // console.log(res.status, typeof res.status);
        this.$router.push("/index");
      }).catch(error => {
        console.log(error);
      })
    },
  },
  created() {
    if (sessionStorage.getItem('username')){
      this.user = sessionStorage.getItem('username')
    }else {
      this.$message.error("当前用户未登录,请登录");
      this.$router.push("/login");
    }

  }
}
</script>

<style scoped>

</style>
