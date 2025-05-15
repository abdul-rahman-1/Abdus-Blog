// Global variable to hold blogs data
window.blogData = [];

// Function to fetch blogs from API
function fetchBlogs() {
  fetch('https://abdus-api.up.railway.app/api/blogs')
    .then(response => response.json())
    .then(data => {
      window.blogData = data;  // Store globally
      renderBlogs(data);
    })
    .catch(error => {
      console.error('Error fetching blogs:', error);
      const container = document.getElementById('blog-list');
      container.innerHTML = '<p>Failed to load blogs. Please try again later.</p>';
    });
}

// Function to render blogs on the page
function renderBlogs(blogs) {
  const container = document.getElementById('blog-container');
  if (!blogs.length) {
    container.innerHTML = '<p>No blogs available at the moment.</p>';
    return;
  }

  container.innerHTML = blogs.map((blog, index) => `
    <div class="col-md-6 col-lg-4 mb-4">
      <div class="card h-100 shadow-sm">
        <img
          src="${blog.image_base64 || 'https://via.placeholder.com/350x200?text=No+Image'}"
          class="card-img-top"
          alt="${blog.title}"
          style="height: 200px; object-fit: cover;"
        />
        <div class="card-body d-flex flex-column">
          <h5 class="card-title">${blog.title}</h5>
          <p class="card-text">${blog.short_content}</p>
          <small class="text-muted mb-2">${new Date(blog.date).toLocaleDateString()}</small>
          <button class="btn btn-primary mt-auto" onclick="openBlogModal(${index})">Read More</button>
        </div>
      </div>
    </div>
  `).join('');
}

// Function to open the modal and populate content
function openBlogModal(index) {
  const blog = window.blogData[index];
  if (!blog) return;

  document.getElementById('blogModalLabel').textContent = blog.title;
  const modalImage = document.getElementById('modalImage');
  modalImage.src = blog.image_base64 || 'https://via.placeholder.com/700x400?text=No+Image';
  modalImage.alt = blog.title;

  // If your content might contain HTML, use innerHTML, else use textContent
  document.getElementById('modalContent').innerHTML = blog.content;

  // Show the modal using Bootstrap's jQuery plugin
  $('#blogModal').modal('show');
}

// Call fetchBlogs on page load
document.addEventListener('DOMContentLoaded', fetchBlogs);
