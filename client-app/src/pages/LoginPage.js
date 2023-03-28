import {React} from 'react'
import {Link} from 'react-router-dom'
import university_background from '../utilities/university_background.jpg'
import login from './LoginPage.module.css'

function LoginPage({setLoginStatus}) {
  const onClickLogin=()=>{
    setLoginStatus(true)
  }

  return (
    <div className={login.background}>
      <img src={university_background} alt=''></img>
      <form className={login.wrapper}>
        <input className={login.email} type="text" placeholder='email'></input>
        <input className={login.password} type="password" placeholder='password'></input>
        <div className={login.buttons}>
          <button className={login.loginbtn} type='button' onClick={() => onClickLogin()}>Log In</button>
          <button className={login.googlebtn}>Google</button>
        </div>
        <div className={login.links}>
          <Link className={login.signup} to='/signup'>Don't have an account?</Link>
          <Link>Forgot password?</Link>
        </div>
      </form>
    </div>
  )
}

export default LoginPage