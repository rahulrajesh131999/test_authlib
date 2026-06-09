"use client"
import React, { useState } from 'react'


const Loginform = () => {

    const [formData, setFormData] = useState({
        email : "",
        password : ""
    })

    const {email, password} = formData;

    const onchangeHandler = (e:React.ChangeEvent<HTMLInputElement>) =>{
        setFormData((prevdata)=>({
            ...prevdata,
            [e.target.name] : e.target.value
        }))
    }

    const onSubmitHandler = async(e:React.SubmitEvent<HTMLFormElement>)=>{
        
    }

  return (
    <div className='flex flex-col '>
        <h1 className='font-bold text-5xl'>Login</h1>
        <form onSubmit={onSubmitHandler} className='flex flex-col gap-5'>
            <input type="email"  value={email} onChange={onchangeHandler} name='email' placeholder='abc@email.com' className='border pl-2.5 py-3 rounded-md'/>
            <input type="password" value={password} onChange={onchangeHandler} name='password' placeholder='********' className='border pl-2.5 py-3 rounded-md'/>
            <button type='submit'></button>
        </form>
    </div>
  )
}

export default Loginform