import { useState } from 'react'
import Employees from './components/Employees'
import Attendance from './components/Attendance'

function App() {
  const [activeTab, setActiveTab] = useState('employees')

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-gray-900">HRMS Lite</h1>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 py-6">
        <div className="bg-white rounded-lg shadow">
          <div className="border-b border-gray-200">
            <nav className="flex -mb-px">
              <button
                onClick={() => setActiveTab('employees')}
                className={`px-6 py-3 text-sm font-medium border-b-2 ${
                  activeTab === 'employees'
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                Employees
              </button>
              <button
                onClick={() => setActiveTab('attendance')}
                className={`px-6 py-3 text-sm font-medium border-b-2 ${
                  activeTab === 'attendance'
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                Attendance
              </button>
            </nav>
          </div>

          <div className="p-6">
            {activeTab === 'employees' ? <Employees /> : <Attendance />}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
