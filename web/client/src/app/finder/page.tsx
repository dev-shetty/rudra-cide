import UserSearch from "@/components/user-search"

export default function SearchPage() {
  return (
    <section className="grid mx-auto min-h-screen px-4 md:px-6 py-6 md:py-12 w-1/2">
      <div className="flex flex-col items-center justify-center space-y-4">
        <div>
          <h1 className="text-7xl font-bold tracking-tighter mb-8 border border-black px-8 py-4">
            Rudra-Cide
          </h1>
          <p className="-mt-12 relative -mr-12 z-1 text-right w-fit ml-auto px-2 py-1 bg-white rounded-md border border-black">
            User Finder
          </p>
        </div>
        <div className="w-full grid gap-12">
          <UserSearch />
        </div>
      </div>
    </section>
  )
}
