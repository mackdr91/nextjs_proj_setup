import os

def write_layout_content(project_dir):
    layout_file_path = os.path.join(project_dir, "app", "layout.jsx")
    layout_content = """
import '@/assets/styles/globals.css';

export const metadata = {
    title: '',
    description: '',
    keywords: '',
    description: '',
}
const MainLayout = ({ children }) => {
    return (
    <html>
        <body>
            <main>
                {children}
            </main>

        </body>
    </html> );
}

export default MainLayout;
"""
    with open(layout_file_path, "w") as f:
        f.write(layout_content)
    print(f"Added content to {layout_file_path}")

def write_page_content(project_dir):
    page_file_path = os.path.join(project_dir, "app", "page.jsx")
    page_content = """

const HomePage = () => {

    return ( <div>
        <h1>Home Page</h1>
    </div> );
}

export default HomePage;
"""
    with open(page_file_path, "w") as f:
        f.write(page_content)
    print(f"Added content to {page_file_path}")


def write_about_content(project_dir):
    about_file_path = os.path.join(project_dir, "app", "about", "page.jsx")
    about_content = """
const AboutPage = () => {
    return ( <div>
        <h1>About Us</h1>
        <p>Welcome to the About Us page. Here is where we tell our story.</p>
    </div> );
}

export default AboutPage;
"""
    # Ensure the "about" directory exists before writing
    os.makedirs(os.path.dirname(about_file_path), exist_ok=True)

    with open(about_file_path, "w") as f:
        f.write(about_content)
    print(f"Added content to {about_file_path}")


def write_contact_content(project_dir):
    contact_file_path = os.path.join(project_dir, "app", "contact", "page.jsx")
    contact_content = """
const ContactPage = () => {
    return ( <div>
        <h1>Contact Us</h1>
        <p>Feel free to reach out to us.</p>
    </div> );
}
export default ContactPage;
"""
    # Ensure the "contact" directory exists before writing
    os.makedirs(os.path.dirname(contact_file_path), exist_ok=True)

    with open(contact_file_path, "w") as f:
        f.write(contact_content)
    print(f"Added content to {contact_file_path}")

def write_services_content(project_dir):
    services_file_path = os.path.join(project_dir, "app", "services", "page.jsx")
    services_content = """
const ServicesPage = () => {
    return ( <div>
        <h1>Services</h1>
        <p>We offer a variety of services.</p>
    </div> );
}

export default ServicesPage;
"""
    # Ensure the "services" directory exists before writing
    os.makedirs(os.path.dirname(services_file_path), exist_ok=True)

    with open(services_file_path, "w") as f:
        f.write(services_content)
    print(f"Added content to {services_file_path}")

def write_styles_content(project_dir):
    styles_file_path = os.path.join(project_dir, "assets", "styles", "globals.css")
    services_content = """
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
"""
    # Ensure the "services" directory exists before writing
    os.makedirs(os.path.dirname(styles_file_path), exist_ok=True)

    with open(styles_file_path, "w") as f:
        f.write(services_content)
    print(f"Added content to {styles_file_path}")


def write_taiwind_content(project_dir):
    tailwind_file_path = os.path.join(project_dir, "tailwind.config.js")

    tailwind_content = """
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
      },
      gridTemplateColumns: {
       '70/30': '70% 28%',
      },
    },
  },
  plugins: [],
};
"""

    with open(tailwind_file_path, "w") as f:
        f.write(tailwind_content)
    print(f"Added content to {tailwind_file_path}")


def write_not_found_content(project_dir):
    not_found_file_path = os.path.join(project_dir,"app", "not-found.jsx")

    not_found_content = """
import Link from "next/link";
import { FaExclamationTriangle } from "react-icons/fa";

const NotFoundPage = () => {
  return (
    <section className="min-h-screen flex items-center">
      <div className="container m-auto max-w-2xl py-24">
        <div className="flex justify-center">
          <FaExclamationTriangle className="text-5xl text-red-500" />
        </div>
        <div className="text-center">
          <h4 className="text-2xl font-bold mt-2 mb-2">
            Sorry, there is nothing here
          </h4>
          <Link href="/">Go Back Home</Link>
        </div>
      </div>
    </section>
  );
};

export default NotFoundPage;
"""

    with open(not_found_file_path, "w") as f:
        f.write(not_found_content)
    print(f"Added content to {not_found_file_path}")
