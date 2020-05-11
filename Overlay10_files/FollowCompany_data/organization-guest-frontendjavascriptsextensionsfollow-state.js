/* global IN */
let companyId, followUrl, followText, followingText, isFollowing, isVertical, csrfToken;

/**
 * Sets the follow state dependent on the return result of follow submit request
 * @public
 */
function updateFollowState() {
  const xmlHttp = new XMLHttpRequest();

  xmlHttp.onreadystatechange = function () {
    if (xmlHttp.readyState === 4) {
      if (xmlHttp.status === 200) {
        // update state and redirect to prevent clickjacking
        _setFollowState();
        _openOrganizationPage();
      } else {
        // request not successful, don't update follow state and open page
        _openOrganizationPage();
      }
    }
  };
  if (followUrl.length) {
    xmlHttp.open('POST', followUrl, true);
    xmlHttp.setRequestHeader('Csrf-Token', csrfToken);
    xmlHttp.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
    xmlHttp.send(JSON.stringify({'shouldFollow': !isFollowing, 'companyId': companyId}));
  }
}

/**
 * Opens the appropriate company page in a new tab
 * @private
 */
function _openOrganizationPage() {
  // String templates not supported by ie
  const url = document.location.origin + '/company/' + companyId;
  window.open(url, '_blank');
}

/**
 * Takes the document properties currently set and updates them depending on
 * whether the new state should be following on not following and updates the
 * click url appropriately as well
 * @private
 */
function _setFollowState() {
  const selectors = Object.freeze({
    followBtn: 'follow-btn',
    followBtnNoCount: 'follow-btn--no-count',
    followingBtn: 'following-btn',
    followingBtnNoCount: 'following-btn--no-count',
    followBtnVertical: 'follow-btn--vertical',
    followingBtnVertical: 'following-btn--vertical',
    followerCount: '.follower-count'
  });
  const hasFollowCount = !!document.querySelector(selectors.followerCount);

  let followButton;

  // Appropriately update the classes for the button as needed
  if (isFollowing && isVertical) {
    followButton = document.getElementsByClassName(selectors.followingBtnVertical)[0];
    followButton.className = selectors.followBtnVertical;
  } else if (!isFollowing && isVertical) {
    followButton = document.getElementsByClassName(selectors.followBtnVertical)[0];
    followButton.className = selectors.followingBtnVertical;
  } else if (isFollowing && hasFollowCount) {
    followButton = document.getElementsByClassName(selectors.followingBtn)[0];
    followButton.className = selectors.followBtn;
  } else if (!isFollowing && hasFollowCount) {
    followButton = document.getElementsByClassName(selectors.followBtn)[0];
    followButton.className = selectors.followingBtn;
  } else if (isFollowing) {
    followButton = document.getElementsByClassName(selectors.followingBtnNoCount)[0];
    followButton.className = selectors.followBtnNoCount;
  } else {
    followButton = document.getElementsByClassName(selectors.followBtnNoCount)[0];
    followButton.className = selectors.followingBtnNoCount;
  }

  // Set the button text, url to fire when clicked, and toggle following status
  followButton.innerText = isFollowing ? followText : followingText;
  isFollowing = !isFollowing;
}

/**
 * Sets the inital follow state properties on the document on page load
 * @public
 */
function initFollowState() {
  // Set onclick handler for button
  const button = document.querySelector('button');
  button.onclick = updateFollowState;

  // Set document properties with server side values stored in code tag
  const code = document.querySelector('code');
  companyId = code.getAttribute('data-company-id');
  followUrl = code.getAttribute('data-follow-url');
  followText = code.getAttribute('data-follow-text');
  followingText = code.getAttribute('data-following-text');
  isFollowing = code.getAttribute('data-is-following') === 'true';
  isVertical = code.getAttribute('data-is-vertical') === 'true';
  csrfToken = code.getAttribute('data-csrf-token');

  // Determine if within an iframe
  let isIframed;
  try {
    isIframed = window.self !== window.top;
  } catch (e) {
    isIframed = true;
  }

  // Set up xdoor server
  if (isIframed) {
    const Server = IN.SDK.Server;
    const server = new Server();
    server.ready();
  }
}

initFollowState();
