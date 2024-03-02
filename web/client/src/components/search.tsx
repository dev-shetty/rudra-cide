"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { SearchIcon } from "lucide-react"
import { FormEvent, useState } from "react"

export default function Search({ inputs }: { inputs: string[] }) {
  const [search, setSearch] = useState<string | null>(null)

  function handleSearch(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    console.log({ search, inputs })
  }
  return (
    <form className="w-full flex items-center space-x-2" onClick={handleSearch}>
      <SearchIcon className="w-4 h-4 opacity-50 mr-4" />
      <Input
        className="w-full flex-1"
        placeholder="Enter the onion URL"
        type="search"
        onChange={(e) => setSearch(e.target.value)}
      />
      <Button type="submit">Search</Button>
    </form>
  )
}
