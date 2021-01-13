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
            <span>用户名：{{user}}</span>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
          update Emp info:
        </h1>
        <form action="" method="post">
          <table cellpadding="0" cellspacing="0" border="0"
                 class="form_table">
            <tr>
              <td valign="middle" align="right">
                id:
              </td>
              <td valign="middle" align="left">
                {{this.$route.params.id}}

              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                name:
              </td>
              <td valign="middle" align="left">
                <input type="text" v-model="emp_list.emp_name" class="inputgri" name="name" value="zhangshan"/>
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                photo:
              </td>
              <td valign="middle" align="left">
                <input type="file" name="photo" ref="photo"/>
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                salary:
              </td>
              <td valign="middle" align="left">
                <input type="text" v-model="emp_list.salary" class="inputgri" name="salary" value="20000"/>
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                age:
              </td>
              <td valign="middle" align="left">
                <input type="text" v-model="emp_list.age" class="inputgri" name="age" value="20"/>
              </td>
            </tr>
          </table>
          <p>
            <el-button type="primary" @click="up_emp">确定修改</el-button>
          </p>
        </form>
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
  name: "UpdateEmp",
  data(){
    return {
      emp_list: [],
      id:'',
      user:'',
      phone:'',
      photo:'',
    }
  },
  created() {
    let use = sessionStorage.getItem('username')
    console.log(use)
    this.user = use

    let num = this.$route.params.id
    // console.log(num);
    this.id = num
    this.axios.get("http://127.0.0.1:8000/app/employeess/" + num + '/',{params:num}).then(res => {
      console.log(res.data.results);
      this.emp_list = res.data.results
      console.log(res.data.results.full_img);
      this.phone = res.data.results.full_img
    }).catch(error => {
      console.log(error)
    })
  },
  methods:{

      up_emp(){
        console.log(this.photo);
        // console.log(this.phone);
        // console.log(111);
        // console.log(this.ref.phone);
        // console.log(this.ref.img);
        console.log(this.emp_list.emp_name)
            let formData = new FormData();
            formData.append("emp_name", this.emp_list.emp_name)
            formData.append("salary", this.emp_list.salary)
            formData.append("age", this.emp_list.age)
            formData.append("img", this.$refs.photo.files[0])
            this.axios({
              url:'http://127.0.0.1:8000/app/employeess/' + this.id + '/',
              method:'patch',
              headers: {
                "content-type": "multipart/form-data"
              },
              data:formData,
            }).then(res => {
              console.log(res);
              this.$message.success("恭喜你，修改成功")
              this.$router.push('/login')
            }).catch(error => {
              console.log(error);
            })
      }
    },
}
</script>

<style scoped>

</style>
