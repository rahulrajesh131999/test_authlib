import Loginform from '@/components/auth/Loginform'
import React from 'react'
import Image from 'next/image'
import stockImage from "@/assets/images/sebastian-svenson-LpbyDENbQQg-unsplash.jpg"

const login = () => {
  return (
    <div className='flex justify-between min-h-screen items-center'>
      <div className="w-100">
        <Loginform/>
      </div>
      <div className='relative  w-150 h-150 overflow-hidden'>
        <Image alt='image' src={stockImage} fill loading="eager" className='w-full h-full object-cover rounded-md'/>
      </div>
    </div>
  )
}

export default login