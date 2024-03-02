"use client"

import Keywords from "@/components/keywords"
import Search from "@/components/search"
import { useState } from "react"

export default function SearchPage() {
  const [inputs, setInputs] = useState<string[]>([""])

  return (
    <section className="grid mx-auto min-h-screen px-4 md:px-6 py-6 md:py-12 w-1/2">
      <div className="flex flex-col items-center justify-center space-y-4">
        <div>
          <h1 className="text-7xl font-bold tracking-tighter mb-8 border border-black px-8 py-4">
            Rudra-Cide
          </h1>
          <p className="-mt-12 relative -mr-8 z-1 text-right w-fit ml-auto px-2 py-1 bg-white rounded-md border border-black">
            Keywords Search
          </p>
        </div>
        <div className="grid gap-12">
          <Search inputs={inputs} />
          <Keywords inputs={inputs} setInputs={setInputs} />
        </div>
      </div>
    </section>
  )
}
