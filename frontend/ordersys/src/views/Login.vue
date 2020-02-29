<template>
  <!--<div>111</div>-->
  <div class="login">
    <el-form class="login-form" label-width="80px" :rules="rules" ref="ruleForm" :model="ruleForm">
      <el-form-item label="用户名" prop="username">
        <el-input type="text" v-model="ruleForm.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="ruleForm.password"></el-input>
      </el-form-item>
      <el-button type="primary" class="btn-login" @click="submitForm('ruleForm')">登陆</el-button>
    </el-form>
  </div>
</template>

<script>

  import {auth} from "../network/auth";
  import {tokenCheck} from "../network/tokenCheck";


  export default {
    name: "Login",
    data() {
      return {
        ruleForm: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            {
              required: true,
              message: '请输入用户名',
              trigger: 'blur'

            }
          ],
          password: [
            {
              required: true,
              message: '请输入密码',
              trigger: 'blur',
              min: 5,
              max: 18
            }
          ]
        },
        token: {
          type: String,
          defaults: 'token'
        }
      }
    },
    methods: {
      submitForm(formName) {
        console.log('111')
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log('发送登陆请求')
            auth(this.ruleForm.username, this.ruleForm.password).then(res => {
              console.log(res)
              if (res.code === 200) {
                // console.log(res)
                let token = res.access_token
                this.setToken(token)
                setTimeout(() => {
                  this.$router.push('/homepage')
                }, 2000)

              } else {
                console.log('登陆失败')
              }
            })
          } else {
            console.log('error')
            return false
          }
        })
      },
      setToken(token) {
        sessionStorage.setItem('token', token)
        // this.$store.commit('setToken', token)
      },
      clearToken() {
        sessionStorage.removeItem('token')
        // this.$store.commit('clearToken')
      }
    },
    created() {
      this.token = sessionStorage.getItem('token')
      tokenCheck(this.token).then(res => {
        console.log(res)
        if (res.code === 200) {
          this.$router.push('/homepage')
        }
      })
    }

  }

</script>

<style scoped>
  .login-form {
    margin: 20px;
  }

  .login {
    width: 30%;
    border: solid 2px #DCDFE6;
    border-radius: 20px;
    text-align: center;
    margin: 180px auto;
  }


</style>

