import { RetroBarcodePage } from './app.po';

describe('retro-barcode App', () => {
  let page: RetroBarcodePage;

  beforeEach(() => {
    page = new RetroBarcodePage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
