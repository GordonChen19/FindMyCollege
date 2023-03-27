import {useState} from 'react'
import navbar from './Navbar.module.css';
import universityhaticon from '../utilities/universityhaticon.png'
import {Link} from 'react-router-dom';

function Navbar() {
  const [loginStatus, setLoginStatus] = useState(false)

  return (
    <div className={navbar.navbarwrapper}>      
    <Link className={navbar.logoheader} to='/'>
      <img src={universityhaticon} className={navbar.logo} alt='FindMyCollege Logo'/>
      <h1 className={navbar.header}>FindMyCollege</h1>
    </Link>
      <div className={navbar.navbarlinks}>
        <Link className={navbar.testlink} to='/test'>Take the Test</Link>
        {loginStatus ? 
        <Link to='/profile'><button className={navbar.profilebtn}>PROFILE</button></Link> : 
        <div className={navbar.loginsignup}>
        <Link to='/login' className={navbar.loginbtn} onClick={() => setLoginStatus(true)}>Login</Link>
          <Link to='/signup'><button className={navbar.signupbtn}>SIGN UP</button></Link>
        </div>
        
        }
      </div>
    </div>
  )
}

export default Navbar