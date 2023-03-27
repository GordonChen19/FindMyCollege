import React from 'react'
import homepage from './HomePage.module.css'
import uni_bg from '../utilities/university_background.jpg'
import uni_student from '../utilities/university_student.jpg'

function HomePage() {
  return (
    <div>
      <img className={homepage.background} src={uni_bg} alt='Background of a university'/>
      <div className={homepage.wrapper}></div>
      <img className={homepage.student} src={uni_student} alt='University students'/>
      <div className={homepage.title}>
        <h1>UNSURE WHERE TO GO NEXT<br></br> IN YOUR ACADEMIC JOURNEY?</h1>
      </div>
      <div className={homepage.info}>
        <h3>
          LET US FIND YOU THE UNIVERSITY OF YOUR <span>DREAMS</span>
        </h3>
        <p>
          FindMyCollege takes into account your academic portfolio,<br></br>
          location preferences and RIASEC personality type<br></br>
          to determine the best university course for you!
        </p>
      </div>
    </div>
  )
}

export default HomePage