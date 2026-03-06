import './globals.css';

export const metadata = {
  title: 'AI Global News Admin',
  description: 'Admin dashboard for source and job status'
};

export default function RootLayout({ children }) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
