"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { SearchIcon } from "lucide-react"
import { useRouter } from "next/navigation"
import { FormEvent, useState } from "react"

export default function UserSearch() {
  const [user, setUser] = useState<string | null>(null)
  const [keyword, setKeyword] = useState<string | null>(null)
  const router = useRouter()

  async function handleSearch(e: FormEvent<HTMLFormElement>) {
    e.preventDefault()
    router.refresh()
    router.push(
      `/finder/result?${new URLSearchParams({
        username: user!,
        key: keyword!,
      })}`
    )
  }

  return (
    <form
      className="w-full flex items-center space-x-2"
      onSubmit={handleSearch}
    >
      <SearchIcon className="w-4 h-4 opacity-50 mr-4" />
      <Input
        className="w-full flex-1"
        placeholder="Enter the username"
        type="text"
        onChange={(e) => setUser(e.target.value)}
      />
      <Input
        className="w-full flex-1"
        placeholder="Keyword to search"
        type="text"
        onChange={(e) => setKeyword(e.target.value)}
      />
      <Button type="submit">Find</Button>
    </form>
  )
}
