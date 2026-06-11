"use client"
import React from 'react'

import {endpoints} from "@/services/api"
import { useRouter } from 'next/navigation'

const dashboard = () => {

  const router = useRouter()

  const logoutHandler = async() =>{
    const response = await fetch(endpoints.LOGOUT_API,{
      method : "GET",
      credentials: "include"
    })

    if(!response.ok){
      throw new Error("failed to log out")
    }

    router.push("/")

  }

  return (
    <div className='min-h-screen flex flex-col gap-5 items-center justify-center'>
      <iframe width="860" height="515"  src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&si=_oBjMy_vzh2aLmUe&amp;controls=0" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>
      <button onClick={logoutHandler} className='hover:underline cursor-pointer'>logout</button>
    </div>
  )
}

export default dashboard