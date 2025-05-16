    document.addEventListener('DOMContentLoaded', () => {
      const container = document.getElementById('news-container');
      let modals = document.getElementById('modals-container');
      if (!modals) {
        modals = document.createElement('div');
        modals.id = 'modals-container';
        document.body.appendChild(modals);
      }

      fetch('https://abdus-api.up.railway.app/api/news', { mode: 'cors' })
        .then(res => {
          if (!res.ok) throw new Error(`Status ${res.status}`);
          return res.json();
        })
        .then(newsData => {
          container.innerHTML = ''; // clear loading
          if (!newsData.length) {
            container.innerHTML = '<p class="text-center w-100">No news available.</p>';
            return;
          }

          newsData.forEach((item, idx) => {
            // Card
            const col = document.createElement('div');
            col.className = 'col-md-4 mb-4';
            col.innerHTML = `
              <div class="card h-100 shadow-sm">
                <div class="card-body d-flex flex-column">
                  <h5 class="card-title">${item.title}</h5>
                  <small class="text-muted mb-2">${new Date(item.date).toLocaleDateString()}</small>
                  <p class="card-text flex-grow-1">${item.summary}</p>
                  <button class="btn btn-primary align-self-start" onclick="$('#modal${idx}').modal('show')">Read Issue</button>
                </div>
              </div>
            `;
            container.appendChild(col);

            // Build modal content
            let sectionsHtml = '';
            if (Array.isArray(item.sections)) {
              item.sections.forEach(sec => {
                sectionsHtml += `<h6>${sec.heading}</h6><p>${sec.content.replace(/\n/g, '<br>')}</p>`;
              });
            }

            const modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.id = `modal${idx}`;
            modal.tabIndex = -1;
            modal.setAttribute('role', 'dialog');
            modal.innerHTML = `
              <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title">${item.title}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    ${sectionsHtml}
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                  </div>
                </div>
              </div>
            `;
            modals.appendChild(modal);
          });
        })
        .catch(err => {
          console.error('Error fetching news:', err);
          container.innerHTML = '<p class="text-center w-100">Failed to load news. Please try again later.</p>';
        });
    });