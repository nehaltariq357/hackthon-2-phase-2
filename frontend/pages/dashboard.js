import dynamic from 'next/dynamic';

// Dynamically import the Dashboard component to avoid SSR issues
const Dashboard = dynamic(() => import('../src/pages/Dashboard'), {
  ssr: false
});

export default function DashboardPage() {
  return <Dashboard />;
}