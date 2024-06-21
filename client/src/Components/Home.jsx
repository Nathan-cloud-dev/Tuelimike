// src/components/Home.js
import React from 'react';

const Home = () => {
  return (
    <div>
      {/* Hero section */}
      <section className="bg-gray-900 text-white py-24">
        <div className="container mx-auto text-center">
          <h1 className="text-4xl font-bold mb-4">Welcome to CourseShop</h1>
          <p className="text-lg mb-8">Explore a wide range of courses in various categories.</p>
          <a href="#" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
            Explore Courses
          </a>
        </div>
      </section>

      {/* Featured Courses section */}
      <section className="py-16">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-8">Featured Courses</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Example course card */}
            <div className="bg-white shadow-lg rounded-lg overflow-hidden">
              <img src="course1.jpg" alt="Course" className="w-full h-64 object-cover" />
              <div className="p-6">
                <h3 className="font-bold text-xl mb-2">Course Title</h3>
                <p className="text-gray-600 mb-4">Instructor: John Doe</p>
                <p className="text-gray-700 mb-4">Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                <a href="#" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
                  View Course
                </a>
              </div>
            </div>
            {/* Repeat for other featured courses */}
          </div>
        </div>
      </section>

      {/* Categories section */}
      <section className="bg-gray-200 py-16">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-8">Explore by Categories</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Example category */}
            <div className="bg-white shadow-lg rounded-lg overflow-hidden flex flex-col items-center justify-center">
              <img src="tech-icon.png" alt="Technology" className="w-20 h-20 mb-4" />
              <h3 className="text-xl font-bold mb-2">Technology</h3>
              <a href="#" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
                View Courses
              </a>
            </div>
            {/* Repeat for other categories */}
          </div>
        </div>
      </section>

      {/* Footer section */}
      <footer className="bg-gray-800 text-white py-12">
        <div className="container mx-auto flex flex-col md:flex-row justify-between">
          <div className="mb-8 md:w-1/4">
            <h3 className="text-xl font-bold mb-4">About CourseShop</h3>
            <p>CourseShop is an e-learning platform offering a wide range of courses.</p>
          </div>
          <div className="mb-8 md:w-1/4">
            <h3 className="text-xl font-bold mb-4">Contact Us</h3>
            <p>Email: info@courses.com</p>
            <p>Phone: +123 456 7890</p>
          </div>
          <div className="mb-8 md:w-1/4">
            <h3 className="text-xl font-bold mb-4">Links</h3>
            <ul>
              <li><a href="#" className="text-white hover:text-gray-300">Privacy Policy</a></li>
              <li><a href="#" className="text-white hover:text-gray-300">Terms of Service</a></li>
            </ul>
          </div>
          <div className="md:w-1/4">
            <h3 className="text-xl font-bold mb-4">Subscribe to Our Newsletter</h3>
            <form className="flex">
              <input type="email" className="px-4 py-2 border border-gray-300 rounded-l focus:outline-none" placeholder="Enter your email" />
              <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-r">
                Subscribe
              </button>
            </form>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Home;