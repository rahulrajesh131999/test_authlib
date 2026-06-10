import Registerform from '@/components/auth/Registerform'
import React from 'react'
import Image from 'next/image'
import stockImage from "@/assets/images/antipolygon-youtube-l6SwTEW2i9I-unsplash.jpg"

const login = () => {
  return (
    <div className='flex justify-between min-h-screen items-center'>
      <div className="w-100">
        <Registerform/>
      </div>
      <div className='relative  w-150 h-150 overflow-hidden'>
        <Image alt='image' src={stockImage} loading="eager" fill className='w-full h-full object-cover rounded-md'/>
      </div>
    </div>
  )
}

export default login