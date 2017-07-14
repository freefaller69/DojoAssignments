import { LayoutProjectPage } from './app.po';

describe('layout-project App', () => {
  let page: LayoutProjectPage;

  beforeEach(() => {
    page = new LayoutProjectPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
