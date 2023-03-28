import {React} from 'react'
import university_background from '../utilities/university_background.jpg'
import signup from './SignUpPage.module.css'

function SignUpPage() {
  return (
    <div className={signup.background}>
      <img src={university_background} alt=''></img>
      <form className={signup.wrapper}>
        <input className={signup.email} type="text" placeholder='email'></input>
        <input className={signup.username} type='text' placeholder='username'></input>
        <input className={signup.password} type="password" placeholder='password'></input>
        <button className={signup.signupbtn} type='button'>Create Your Account</button>
      </form>
    </div>
  )
}

export default SignUpPage