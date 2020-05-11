/* global IN */
// This file is used to initialize the new Follow Company Widget for XDoor
(function () {
  const Tag = IN.SDK.Tag,
    EmbeddedWindow = IN.SDK.EmbeddedWindow,
    Client = IN.SDK.Client;

  /**
   * Creates the xdoor tag for follow company
   * @param {Object} node
   * @param {Object} core
   * @returns {Object} The tag object
   */
  function FollowCompany(node, core) {
    const tag = new Tag(node, core);
    const tagCounter = tag.attributes.counter;
    const tagId = tag.attributes.id;

    const extensionUrlPrefix = IN.options.get('urls.www.linkedin.com') + '/pages-extensions/FollowCompany';
    const extensionUrl = IN.SDK.addParams(extensionUrlPrefix, {
      id: tagId,
      counter: tagCounter
    });
    const extensionFrame = new EmbeddedWindow(extensionUrl);
    /* eslint-disable no-unused-vars */
    const client = new Client(extensionFrame);

    tag.insert(extensionFrame.self);
    /* eslint-enable no-unused-vars */
    return tag;
  }

  IN.tags.add('FollowCompany', FollowCompany);
})();
