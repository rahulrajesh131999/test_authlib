"use client"
import React, { useState } from 'react'

import googlesvg from "@/assets/svgs/google-icon-logo-svgrepo-com.svg"
import { loginapi } from '@/services/operations/authAPI'
import { useRouter } from 'next/navigation'
import { useAppDispatch,useAppSelector } from '@/reducer/reducerHooks'
import { setUser } from '@/slices/auth.slice'


const Loginform = () => {

    const [formData, setFormData] = useState({
        email : "",
        password : ""
    })

    const {email, password} = formData;
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
        const data = await loginapi({email,password})
        if(!data){
            console.log("failed to login")
            return
        }

        dispatch(setUser(data.user))

        router.push("/dashboard")
    }

     const onClickGoogleHandler = ()=>{
          window.location.assign("https://test-authlib-server.onrender.com/api/v1/auth/login/google") 
        }

  return (
    <div className='flex flex-col w-full'>
        <div className='py-5 flex flex-col gap-2 select-none'>
        <h1 className='font-semibold text-[3rem] leading-none'>Welcome Back</h1>
        <p className='text-sm'>Enter your email and password to access your account</p>
        </div>
        <form onSubmit={onSubmitHandler} className='flex flex-col gap-8'>
            <input type="email"  value={email} onChange={onchangeHandler} name='email' placeholder='abc@email.com' className='border pl-2.5 py-3 border-t-0 border-l-0 border-r-0'/>
            <input type="password" value={password} onChange={onchangeHandler} name='password' placeholder='********' className='border pl-2.5 py-3 border-t-0 border-l-0 border-r-0'/>
            <button type='submit' className='bg-blue-500 py-3 rounded-md font-medium text-amber-50 hover:bg-blue-700 cursor-pointer transition-all duration-500'>login</button>
        </form>
        <p className='text-sm select-none pt-4'>Don't have and account? <a className='font-semibold hover:underline transition-all duration-300' href="/">Sign up</a></p>
        <div className='h-px bg-black my-5'></div>
        <button onClick={onClickGoogleHandler} className='border cursor-pointer hover:bg-blue-200 transition-all duration-300 flex items-center justify-center gap-2 border-gray-700 py-3 group rounded-md'><span className='flex items-center justify-center'><img loading='eager' src={googlesvg.src} alt="logo" className='h-5 w-5 group-hover:rotate-360 duration-700 transition-all'/></span>Sign in with Google</button>
    </div>
  )
}

export default Loginform