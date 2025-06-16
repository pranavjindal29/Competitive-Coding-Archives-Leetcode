const cancellable = <T>(generator: Generator): [() => void, Promise<T>] => {
  let cancel: () => void;
  const cancelPromise = new Promise<never>((_, reject) => {
    cancel = () => reject("Cancelled");
  });
  // Every Promise rejection has to be caught.
  cancelPromise.catch(() => {});

  const promise = (async (): Promise<T> => {
    let next = generator.next();
    while (!next.done) {
      try {
        next = generator.next(await Promise.race([next.value, cancelPromise]));
      } catch (e) {
        next = generator.throw(e);
      }
    }
    return next.value;
  })();

  return [cancel, promise];
};