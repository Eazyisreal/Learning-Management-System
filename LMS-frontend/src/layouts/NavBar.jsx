function NavBar()
{
    return(
        <div className="bg-white p-9">
        <header className="flex justify-between">
            <h2 className="">WeTeach</h2>
            <nav className="inline-block">
            <ul className="">
                <li className=""><a href="">Buy Now</a></li>
                <li  className=""><a href="">For Organisations </a></li>
                <li className=""><a href="#">Contact us</a></li>
                <li className=""><a href="#">Company</a></li>
            </ul>
            </nav>
            <div className="flex gap-2">
            <a className=""  id="cta" href="#"><button type="submit">Sign in</button></a>
            <a className=""  id="cta" href="#"><button type="submit">Get Started</button></a>
            </div>
        </header>    
        </div>
    )
}

export default NavBar