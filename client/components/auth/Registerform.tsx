"use client"
import React, { useState } from 'react'

import googlesvg from "@/assets/svgs/google-icon-logo-svgrepo-com.svg"
import { registerapi } from '@/services/operations/authAPI'
import { useRouter } from 'next/navigation'
import {useAppDispatch,useAppSelector} from "@/reducer/reducerHooks"
import { setUser } from '@/slices/auth.slice'


const Registerform = () => {

    const [formData, setFormData] = useState({
      fullName : "",
      email : "",
      password : "",
      confirmPassword : ""
    })

    const {fullName, email, password, confirmPassword } = formData;
    const router = useRouter()
    const dispatch = useAppDispatch()

    const onchangeHandler = (e:React.ChangeEvent<HTMLInputElement>) =>{
        setFormData((prevdata)=>({
            ...prevdata,
            [e.target.name] : e.target.value
        }))
    }

    const onSubmitHandler = async(e:React.SubmitEvent<HTMLFormElement>)=>{

      e.preventDefault()

        if(password != confirmPassword){
          console.error("password and confirm password does not match")
          return
        }

        if (password.length < 8 ){
          console.log("password length is less than 8")
          return
        }

       const data =  await registerapi({fullName, email, password,confirmPassword})

       if(!data){
        throw new Error("failed to register user")
       }

       dispatch(setUser(data.user))
       router.push("/dashboard")
    }

        const onClickGoogleHandler = ()=>{
          window.location.assign("http://localhost:8000/api/v1/auth/login/google")
        }

  return (
    <div className='flex flex-col w-full'>
        <div className='py-5 flex flex-col gap-2 select-none'>
        <h1 className='font-semibold text-[3rem] leading-none'>Get Started</h1>
        <p className='text-sm'>Welcome to application - Let's get started</p>
        </div>
        <form onSubmit={onSubmitHandler} className='flex flex-col gap-4'>
            <input type="text" value={fullName} onChange={onchangeHandler} name='fullName' placeholder='John Doe' className='border pl-2.5 py-3 border-t-0 border-l-0 border-r-0'/>
            <input type="email"  value={email} onChange={onchangeHandler} name='email' placeholder='abc@email.com' className='border pl-2.5 py-3 border-t-0 border-l-0 border-r-0'/>
            <input type="password" value={password} onChange={onchangeHandler} name='password' placeholder='********' className='border pl-2.5 py-3 border-t-0 border-l-0 border-r-0'/>
            <input type="password" value={confirmPassword} onChange={onchangeHandler} name='confirmPassword' placeholder='********' className='border pl-2.5 py-3 border-t-0 border-l-0 border-r-0'/>
            <button type='submit' className='bg-blue-500 py-3 rounded-md font-medium text-amber-50 hover:bg-blue-700 cursor-pointer transition-all duration-500'>sign up</button>
        </form>
        <p className='text-sm select-none pt-4'>Already a member? <a className='font-semibold hover:underline transition-all duration-300' href="/login">login</a></p>
        <div className='h-px bg-black my-5'></div>
        <button onClick={onClickGoogleHandler} className='border cursor-pointer hover:bg-blue-200 transition-all duration-300 flex items-center justify-center gap-2 border-gray-700 py-3 group rounded-md'><span className='flex items-center justify-center'><img loading='eager' src={googlesvg.src} alt="logo" className='h-5 w-5 group-hover:rotate-360 duration-700 transition-all'/></span>Sign in with Google</button>
    </div>
  )
}

export default Registerform